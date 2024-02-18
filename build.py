from argparse import ArgumentParser
from pathlib import Path
import shlex
import shutil
import subprocess
from typing import Iterable, Union, Optional, List


class ShellCommand:
    parts: Iterable[Union[str, Path]]
    cwd: Optional[Path]

    def __init__(self, *parts: Union[str, Path], cwd: Optional[Path] = None):
        self.parts = parts
        self.cwd = cwd
    
    @property
    def parts_str(self) -> str:
        return shlex.join([str(part) for part in self.parts])
    
    @property
    def cwd_str(self) -> Optional[str]:
        return None if not self.cwd or self.cwd == Path.cwd() else str(self.cwd)

    
    def __str__(self):
        parts_str = self.parts_str
        cwd_str = self.cwd_str

        if self.cwd:
            return f"(cd {cwd_str} && {parts_str})"
        
        return parts_str
    
    def show(self):
        print(str(self))
    
    def run(self):
        self.show()
        subprocess.run(self.parts_str, cwd=self.cwd_str, shell=True)


def main(
    lobster_root: Path,
    entry: Path,
    html: Path,
    out_dir: Path,
    serve: bool,
    no_run: bool,
) -> List[str]:

    lobster_executable = lobster_root.joinpath("bin", "lobster")
    wasm_root = lobster_root.joinpath("dev", "emscripten")

    commands = [
        ShellCommand(lobster_executable, "--cpp", entry),
        ShellCommand("make", "-j8", cwd=wasm_root),
        ShellCommand("cp", "-r", wasm_root, out_dir),
        ShellCommand("cp", html, out_dir.joinpath("index.html")),
    ]

    if serve:
        commands.append(
            ShellCommand(
                "python3",
                "-m",
                "http.server",
                "8080",
                "--bind",
                "127.0.0.1",
                "--directory",
                out_dir
            )
        )

    if not no_run:
        print()

        try:
            shutil.rmtree(out_dir)
        except FileNotFoundError:
            pass

        for command in commands:
            command.run()
    
    else:
        for command in commands:
            command.show()

    return "\n".join(str(command) for command in commands)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument(
        "--lobster_root",
        type=Path,
        help="The root directory of the Lobster language.",
        default=Path("~/lobster/").expanduser(),
    )

    parser.add_argument(
        "--entry",
        type=Path,
        help="The Lobster entry script.",
        default=Path("./src/main.lobster"),
    )

    parser.add_argument(
        "--html",
        type=Path,
        help="The index HTML source file to copy to out-dir.",
        default=Path("./src/index.html"),
    )

    parser.add_argument(
        "--out-dir",
        type=Path,
        help="The output directory for HTML, WASM, JS, etc.",
        default=Path("./emscripten"),
    )

    parser.add_argument(
        "--serve",
        action="store_true",
        help="If provided, serve out-dir over an HTTP server.",
    )

    parser.add_argument(
        "--no-run",
        action="store_true",
        help="If provided, only print the build script and don't run.",
    )

    args = parser.parse_args()

    main(
        lobster_root=args.lobster_root,
        entry=args.entry,
        html=args.html,
        out_dir=args.out_dir,
        serve=args.serve,
        no_run=args.no_run,
    )
