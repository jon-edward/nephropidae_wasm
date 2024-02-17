from argparse import ArgumentParser
import os
from pathlib import Path
import shlex
import subprocess
from typing import List


def main(
        lobster_root: Path, 
        entry: Path,
        html: Path,
        out_dir: Path,
        serve: bool,
        no_run: bool) -> List[str]:
    
    lobster_executable = str(lobster_root.joinpath("bin", "lobster"))
    default_lpak = str(entry.parent.joinpath("default.lpak"))
    wasm_root = lobster_root.joinpath("dev", "emscripten")
    data = str(lobster_root.joinpath("data"))

    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(out_dir.joinpath("data"), exist_ok=True)

    commands = [
        shlex.join([lobster_executable, "--pak", str(entry)]),
        shlex.join([lobster_executable, "--cpp", str(entry)]),
        shlex.join(["cp", "-r", data, str(out_dir)]),
        shlex.join(["cp", default_lpak, str(out_dir.joinpath("default.lpak"))]),
    ]

    make_command = shlex.join([
        "make",
        "-j8"
    ])

    copy_js_wasm_command = shlex.join([
        "cp",
        str(wasm_root.joinpath("lobster.js")),
        str(wasm_root.joinpath("lobster.wasm")),
        str(wasm_root.joinpath("lobster.data")),
        str(out_dir)
    ])

    copy_html_command = shlex.join(["cp", str(html), str(out_dir.joinpath("index.html"))])

    serve_command = shlex.join([
        "python3", 
        "-m",
        "http.server",
        "8080",
        "--bind",
        "127.0.0.1", 
        "--directory",
        str(out_dir)])

    all_commands = commands + [f"(cd {wasm_root} && {make_command})", copy_js_wasm_command, copy_html_command]

    if serve:
        all_commands.append(serve_command)

    print("\n".join(all_commands))

    if not no_run:
      print()
      
      for command in commands:
          subprocess.run(command, shell=True)

      subprocess.run(make_command, shell=True, cwd=wasm_root)
      subprocess.run(copy_js_wasm_command, shell=True)
      subprocess.run(copy_html_command, shell=True)

      print("Finished building.\n")
      if serve:
          subprocess.run(serve_command, shell=True)
    
    return all_commands


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument(
        "--lobster_root", 
        type=Path, 
        help="The root directory of the Lobster language.", 
        default=Path("~/lobster/").expanduser())
    
    parser.add_argument(
        "--entry",
        type=Path,
        help="The Lobster entry script.",
        default=Path("./src/main.lobster")
    )

    parser.add_argument(
        "--html",
        type=Path,
        help="The index HTML source file to copy to out-dir.",
        default=Path("./src/index.html")
    )

    parser.add_argument(
        "--out-dir",
        type=Path,
        help="The output directory for HTML, WASM, JS, etc.",
        default=Path("./build")
    )

    parser.add_argument(
        "--serve",
        action="store_true",
        help="If provided, serve out-dir over an HTTP server."
    )

    parser.add_argument(
        "--no-run",
        action="store_true",
        help="If provided, only print the build script and don't run."
    )

    args = parser.parse_args()

    main(
        lobster_root=args.lobster_root,
        entry=args.entry,
        html=args.html,
        out_dir=args.out_dir,
        serve=args.serve,
        no_run=args.no_run
    )
