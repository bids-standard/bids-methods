# bids-methods

Repository for templates to generate methods section descriptions of BIDS datasets

These templates use the Mustache templating language: https://mustache.github.io/

## Code style

When some BIDS metadata is used "as is" as a mustache variable,
we kept its original name and use CamelCase.

```mustache
The data acquisition was performed in the {{ InstitutionName }}, {{ InstitutionalDepartmentName }}, {{ InstitutionAddress }}.
```

For some other metadata eventhough we changed their name for the mustache variable.
For some this was to enforce using a more appropriate unit for methods reporting.

For example we do:

```mustache
repetition time, TR= {{ tr }} ms;
```

instead of

```mustache
repetition time, TR= {{ RepetitionTime }} seconds;
```
