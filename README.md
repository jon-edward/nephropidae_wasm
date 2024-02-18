# nephropidae_wasm
This is a simple example that demonstrates building a Lobster project to WebAssembly. 

## Demo
Check out the [live demos](https://jon-edward.github.io/nephropidae_wasm/demos/).

## Requirements
You need a [built binary](http://aardappel.github.io/lobster/getting_started.html) of the [Lobster](https://github.com/aardappel/lobster) language, Python 3.10+, and [Emscripten](https://emscripten.org/docs/getting_started/) added to PATH.

## Usage
[`build.py`](build.py) is the entry point for building a Lobster project to WASM. In the simplest case, you can build your Lobster script (`src/main.lobster`) with `python3 build.py`.

Optionally, you can start an HTTP server from `emscripten/` on `http://127.0.0.1:8080/` after building has completed with the command `python3 build.py --serve`.

See `python3 build.py --help` for other usage.
