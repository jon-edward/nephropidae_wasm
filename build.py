from argparse import ArgumentParser
from pathlib import Path
import shlex
import shutil
import subprocess
from typing import List


def main(
    lobster_root: Path,
    entry: Path,
    html: Path,
    out_dir: Path,
    serve: bool,
    no_run: bool,
) -> List[str]:

    lobster_executable = str(lobster_root.joinpath("bin", "lobster"))
    wasm_root = lobster_root.joinpath("dev", "emscripten")

    compile_cpp_command = shlex.join([lobster_executable, "--cpp", str(entry)])

    make_command = shlex.join(["make", "-j8"])

    copy_html_command = shlex.join(
        ["cp", str(html), str(out_dir.joinpath("index.html"))]
    )

    copy_emscripten_command = shlex.join(["cp", "-r", str(wasm_root), str(out_dir)])

    serve_command = shlex.join(
        [
            "python3",
            "-m",
            "http.server",
            "8080",
            "--bind",
            "127.0.0.1",
            "--directory",
            str(out_dir),
        ]
    )

    if not no_run:
        print()

        try:
            shutil.rmtree(out_dir)
        except FileNotFoundError:
            pass

        subprocess.run(compile_cpp_command, shell=True)
        subprocess.run(make_command, shell=True, cwd=wasm_root)
        subprocess.run(copy_emscripten_command, shell=True)
        subprocess.run(copy_html_command, shell=True)
        
        print("Finished building.\n")

        if serve:
            subprocess.run(serve_command, shell=True)

    return []


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
