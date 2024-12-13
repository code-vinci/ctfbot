# CodeVinciCTF

CodeVinciCTF is a Discord bot designed to streamline the management of Capture the Flag (CTF) events within your team. From organizing challenges to managing roles and sharing updates, CTFBot has you covered.

## Features

- **Challenge Management**: Add, update, and track the status of CTF challenges.
- **Role Management**: Automatically assign roles for team members based on their responsibilities or challenge involvement.
- **Notifications**: Send updates on new challenges, solved challenges, or important announcements.
- **Team Collaboration**: Enhance coordination with commands that simplify teamwork.
- **TODO: CTF Events**: Schedule and track ongoing or upcoming events.

## Getting Started

### Prerequisites

Before setting up CTFBot, ensure you have the following:

- Python (v3.8 or higher)
- Discord.py (v2.0 or higher)
- A Discord bot token (You can obtain one from the [Discord Developer Portal](https://discord.com/developers/applications)).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/code-vinci/ctfbot.git
   cd ctfbot
   ```

3. Configure the bot by creating a `.env` file in the project root:

   ```env
   DISCORD_TOKEN="<token>"
   ```

4. Start the bot:

   ```bash
   docker-compose build
   docker-compose up
   ```

5. Take down the bot:

   ```bash
   docker-compose down --volumes
   ```

## Usage

Invite the bot to your Discord server and use the configured prefix (default: `!`) to interact with it. For example:

- `/create <name>`: Add a new CTF challenge.
- `/create_challenge`: Add new text channel to discuss about challenge.
- `/flag`: Marks the challenge as solved with a 🚩 emoji.
- `/hackerman`: Send a fancy hackerman's gif.

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to reach out with suggestions or issues through the repository's issue tracker. Happy hacking!
