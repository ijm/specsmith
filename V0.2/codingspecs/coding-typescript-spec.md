<!-- markdownlint-disable MD041 -->
## coding-typescript.spec.md: Coding Constraints for TypeScript

### Summary

This document defines the requirements and constraints for writing standalone TypeScript targeting TypeScript 5.0+ that adhere to modern TypeScript conventions, use strict typing features, and follow standard practices for web applications and Chrome extensions.

### Inheritance

This document inherits from:

* [Standard Vocabulary](std.vocab.md)
* [Verification Tags Vocabulary](verification-tags.vocab.md)
* [TECHDOC Structural Specification](techdoc-core.spec.md)

This document conforms to:

* [TECHDOC Specification](techdoc.spec.md)

### Constraints

* TS01 Scripts MUST be compatible with TypeScript version 5.0 or greater. Ⓟ
* TS02 Scripts MUST use strict mode and explicit type checking. Ⓟ
* TS03 Scripts MUST use type annotations for all function definitions, variables, and return types. Ⓟ
* TS04 Scripts MUST conform to standard TypeScript style guidelines. Ⓟ
* TS05 Scripts MAY use features from TypeScript 5.0 and later, including template literal types. Ⓗ
* TS06 Scripts MUST use interfaces over types for object definitions unless using union types or utility types. Ⓟ
* TS07 Scripts MUST NOT use enums; MUST use const objects with 'as const' assertion instead. Ⓟ
* TS08 Scripts SHOULD include a module-level comment describing the purpose and usage. Ⓗ
* TS09 Type annotations MUST use explicit return types for all functions. Ⓟ
* TS10 Scripts MUST NOT use wildcard imports. Ⓟ
* TS11 Functions and variables SHOULD use `camelCase` naming. Ⓗ
* TS12 Classes and interfaces SHOULD use `PascalCase` naming. Ⓗ
* TS13 Files SHOULD use `kebab-case` for directories and `PascalCase` for component files. Ⓗ
* TS14 Scripts MUST use absolute imports with @/ prefix for internal imports. Ⓟ
* TS15 Scripts MUST implement proper error boundaries and error handling. Ⓟ

### Chrome Extension Specific Constraints

* TS20 Chrome extensions MUST use Manifest V3 standards. Ⓟ
* TS21 Message passing MUST use discriminated unions with explicit type definitions. Ⓟ
* TS22 Content scripts MUST not close over variables from outer scope. Ⓟ
* TS23 Content scripts MUST not use imported functions from outer scope. Ⓟ
* TS24 Async injected scripts MUST have wrapped error handling. Ⓟ

### React and UI Constraints

* TS30 Components MUST be functional components with TypeScript interfaces. Ⓟ
* TS31 Components SHOULD use named exports over default exports. Ⓗ
* TS33 Scripts MUST implement proper cleanup in useEffect hooks. Ⓟ
* TS34 Scripts SHOULD use declarative JSX patterns. Ⓗ

### Security Constraints

* TS50 Scripts MUST implement Content Security Policy. Ⓟ
* TS51 Scripts MUST sanitize user inputs. Ⓟ
* TS52 Scripts MUST handle sensitive data properly. Ⓟ
* TS53 Scripts MUST implement proper CORS handling. Ⓟ

### Prohibited Elements

* TS60 Scripts MUST NOT use deprecated TypeScript features. Ⓟ
* TS61 Scripts MUST NOT rely on features only available in TypeScript 5.1 or later without explicit declaration. Ⓟ
* TS62 Scripts MUST NOT use non-standard libraries without explicit declaration. Ⓟ
* TS63 Scripts MUST NOT contain top-level executable code. Ⓟ
* TS64 Scripts SHOULD NOT use try/catch blocks. Ⓟ
* TS65 Scripts SHOULD NOT include comments except for complex logic. Ⓟ
