from django.core.management.base import BaseCommand

from project.apps.rulers.wikipedia_parser_utils import update_all_rulers


class Command(BaseCommand):
    help = 'Update all austria rulers in database from wikipedia'

    def handle(self, *args, **options):
        update_all_rulers()
        self.stdout.write(self.style.SUCCESS('Successfully update all austria rulers'))
