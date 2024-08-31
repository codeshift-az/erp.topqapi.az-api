import logging
import os
from datetime import datetime

from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Shortcut backup command for django-dbbackup"

    logger = logging.getLogger("backup")

    def handle(self, *args, **options) -> None:
        """Handle the command."""

        self.storage_backup()

        self.local_backup()

        self.remove_old_backups()

        self.logger.info("All backups are done.")

    def storage_backup(self):
        """Create a backup in the "dbbackup" storage."""

        self.logger.info("Starting storage backup...")

        call_command("dbbackup", "--clean", "--noinput")
        call_command("mediabackup", "--clean", "--noinput")

        self.logger.info("Backup files are stored in the S3 bucket.")

    def local_backup(self):
        """Create a backup in the local directory."""

        self.logger.info("Starting local backup...")

        if not os.path.exists(f"{settings.BASE_DIR}/backups"):
            os.makedirs(f"{settings.BASE_DIR}/backups")

        open(f"{settings.BASE_DIR}/backups/{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.psql.bin", "w").close()

        call_command(
            "dbbackup",
            f"--output-path={settings.BASE_DIR}/backups/{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.psql.bin",
        )

        open(f"{settings.BASE_DIR}/backups/{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.tar", "w").close()

        call_command(
            "mediabackup",
            f"--output-path={settings.BASE_DIR}/backups/{datetime.now().strftime('%Y-%m-%d_%H%M%S')}.tar",
        )

        self.logger.info("Backup files are stored in the local directory.")

    def remove_old_backups(self):
        """Remove old backups."""

        self.logger.info("Removing old backups...")

        KEEP = settings.DBBACKUP_CLEANUP_KEEP
        KEEP_MEDIA = settings.DBBACKUP_CLEANUP_KEEP_MEDIA

        for backup in sorted(os.listdir(f"{settings.BASE_DIR}/backups"), reverse=True):
            if "psql.bin" in backup:
                KEEP -= 1
                if KEEP < 0:
                    os.remove(f"{settings.BASE_DIR}/backups/{backup}")

            if "tar" in backup:
                KEEP_MEDIA -= 1
                if KEEP_MEDIA < 0:
                    os.remove(f"{settings.BASE_DIR}/backups/{backup}")

        self.logger.info("Old backups are removed.")
