# Encapsulated projects

This directory contains self-contained campaign projects that have their own
entry point, supporting assets, scripts, documentation, and generated output.

Each project should:

- live in its own named directory;
- keep build and verification scripts inside the project;
- keep generated files under the project's own `assets/output/` directory;
- document regeneration and validation in a local `README.md`; and
- avoid placing project-specific scripts or output at the repository root.
