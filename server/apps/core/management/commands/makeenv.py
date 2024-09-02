import os
import re

from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from django.utils.crypto import get_random_string

from server.settings.components import BASE_DIR


class Command(BaseCommand):
    help = "Create a .env file"

    env_file = "config/.env"
    example_file = "config/.env.example"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--noinput",
            action="store_false",
            dest="interactive",
            help="Don't ask for input",
        )

        parser.add_argument(
            "--example",
            action="store",
            help="Path to the example .env file",
        )

        parser.add_argument(
            "--env",
            action="store",
            help="Path to the .env file",
        )

    def handle(self, *args, **options) -> None:
        """Create an .env file from the .env.example file"""

        self.options = options

        if not self.check_overwrite():
            return

        self.stdout.write("Creating .env file...")

        self.create_env_file()

        self.stdout.write(self.style.SUCCESS("Done!"))

    def check_overwrite(self) -> bool:
        """Check if the user wants to overwrite the existing .env file"""
        env_file = self.options.get("env") or self.env_file

        if os.path.exists(BASE_DIR / env_file):
            ans = input(f"File {env_file} already exists. Do you want to overwrite it? (y/n): ")
            if ans.lower() != "y":
                self.stdout.write(self.style.WARNING("Aborted!"))
                return False

        return True

    def create_env_file(self) -> None:
        example_file = self.options.get("example") or self.example_file
        env_file = self.options.get("env") or self.env_file

        with open(BASE_DIR / example_file, "r") as example_file:
            with open(BASE_DIR / env_file, "w") as env_file:
                for line in example_file:
                    if "#" not in line and "=" in line:
                        env_file.write(self.get_env_variable(line))
                    else:
                        env_file.write(line)

    def get_env_variable(self, line: str) -> str:
        """Get the environment variable from the user"""

        key, default = line.split("=")
        key = key.strip()
        default = default.strip()

        return f"{key}={self.get_variable(key, default)}\n"

    def get_variable(self, key: str, default: str) -> str:
        """Get a variable from the user with validation"""
        if "DJANGO_SECRET_KEY" in key:
            return self.get_random_secret_key()

        if "PASSWORD" in key:
            return self.get_random_password()

        if not self.options.get("interactive", True):
            return default

        while True:
            value = input(f"Enter value for {key} (default: {default}): ").strip()

            if not value:
                return default

            if not self.validate(key, value):
                continue

            return value

    def get_random_secret_key(self) -> str:
        return get_random_string(50)

    def get_random_password(self) -> str:
        return get_random_string(12)

    def validate(self, key: str, value: str) -> str:
        """Validate the value"""
        if "DOMAIN" in key:
            return self.validate_domain(value)

        elif "PORT" in key:
            return self.validate_port(value)

        return self.validate_name(value)

    def validate_domain(self, domain: str) -> str:
        """Validate the domain"""
        if not re.match(r"^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$", domain):
            self.stdout.write(self.style.ERROR("Invalid domain. Must be a valid domain"))
            return

        return domain

    def validate_name(self, name: str) -> str:
        """Validate the name"""
        if not name.isidentifier():
            self.stdout.write(self.style.ERROR("Invalid name. Must be a valid Python identifier"))
            return

        return name

    def validate_port(self, port: str) -> str:
        """Validate the port"""
        if not port.isdigit():
            self.stdout.write(self.style.ERROR("Invalid port. Must be a number"))
            return

        return port
