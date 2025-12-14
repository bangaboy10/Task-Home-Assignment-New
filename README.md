# NL → DSL → Strategy Execution Prototype

## Overview
This project demonstrates an end-to-end pipeline that converts
natural language trading rules into a domain-specific language (DSL),
parses them into an AST, generates Python strategy code, and executes
a simple backtest over OHLCV data.

---

## Project Structure
- nl_parser/       : Natural language to structured JSON
- dsl/             : DSL grammar, parser, and AST builder
- codegen/         : AST to Python code generator
- backtest/        : Simple backtest simulator
- data/            : Sample OHLCV dataset
- demo.py          : End-to-end demo script

---

## Setup

```bash
pip install -r requirements.txt


python demo.py
