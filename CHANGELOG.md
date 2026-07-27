# Changelog

## [0.2.0] - 2026-07-28

### Added
- SQLite database integration
- Automatic database initialization
- Conversation repository
- Persistent conversation memory
- Repository pattern for data access

### Changed
- Replaced in-memory conversation history with SQLite persistence
- Conversation service now delegates storage to repository

### Fixed
- Conversation history now survives application restart
