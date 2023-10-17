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

Script/Program files must be valid UTF-8 without BOM.

However, for theoretical computer-science purposes, programs may be treated as abstract data-structures that aren't "unified" nor "split", and therefore need no delimiter, as the concept of a file-system doesn't exist in the theoretical realm.

The standard imposes no restrictions on memory usage. Programs may use as much memory as they request, or as much memory as the impl supports on a given platform.

Impls are encouraged to support inline-flags. This allows retran developers to enable modes/features, without passing impl-specific args to an interpreter. This, in turn, provides a self-contained API, unlike BF programs where all metadata must be specified in different ways to different interpreters (GUI text-boxes, CLI args, fn params, etc...).

For interactive use and/or development purposes, `x` flag must be enabled by default. This allows easier editing and readability. For minification purposes, impls are allowed to disable `x`.
