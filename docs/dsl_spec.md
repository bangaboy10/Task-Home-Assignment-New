# DSL Specification for Trading Strategy Rules

## Overview
This DSL is designed to represent simple trading strategies with
clear entry and exit conditions. It acts as an intermediate
representation between natural language and executable Python code.

The DSL prioritizes clarity, correctness, and ease of parsing.

---

## Structure

A strategy contains two sections:

ENTRY:
<expression>

EXIT:
<expression>

Each expression evaluates to a boolean value per time step.

---

## Supported Fields
- open
- high
- low
- close
- volume

---

## Indicators

### Simple Moving Average (SMA)
Syntax:
SMA(close, 20)

### Relative Strength Index (RSI)
Syntax:
RSI(close, 14)

Indicators are evaluated using rolling window calculations.

---

## Comparison Operators
- >
- <
- >=
- <=
- ==

---

## Boolean Operators
- AND
- OR

Parentheses can be used for nested logic.

---

## Cross Events
Special operators are used for cross conditions:

- CROSSES_ABOVE
- CROSSES_BELOW

Example:
close CROSSES_ABOVE SMA(close, 20)

---

## Time References
- YESTERDAY_HIGH
- YESTERDAY_LOW
- LAST_WEEK(close)

These are resolved during execution.

---

## Examples

### Example 1
ENTRY:
close > SMA(close,20) AND volume > 1000000

EXIT:
RSI(close,14) < 30

### Example 2
ENTRY:
(close > SMA(close,20) AND volume > 1000000)
OR close CROSSES_ABOVE YESTERDAY_HIGH

EXIT:
RSI(close,14) < 30

---

## Assumptions
- Only one position at a time
- ENTRY and EXIT rules are evaluated independently
- Indicators use closing prices unless specified
