# RET
An esoteric programming-language that works like FRACTRAN, but with regular-expressions instead of fraction-lists, and text-input instead of bigints.

## Name

These are the only valid names:
- regexTRAN
- regexpTRAN
- reTRAN
- retran
- reTran

When introducing people to this lang, you should use the longer names, as the short ones may be confused with another software of the same name. After a disambiguating-context has been established, you may use any name, interchangeably.

## Spec

This is the **official specification**. All compliant implementations must follow it. However, it's **very unstable**, so don't take it seriously (yet)

Every retran program is comprised of 2 parts:
- Regular Expression (flavor is implementation-defined)
- Raw string literal (used as replacement for the input)

Implementations are **extremely encouraged** to support *"unified files"*. These files contain both components of the program, separated by some delimiter (usually `//`). If, for any justified reason, the implementation cannot support unified-files, the impl may support split-files (one for regex, another for replacement).

Implementations are also encouraged to support inline-flags. This allows retran developers to enable modes/features, without passing implementation-specific args to an interpreter. This, in turn, provides a self-contained API, unlike BF programs where all metadata must be specified in different ways to different interpreters (GUI text-boxes, CLI args, fn params, etc...).
