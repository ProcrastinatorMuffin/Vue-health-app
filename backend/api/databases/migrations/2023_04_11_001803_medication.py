"""Medication Migration."""

from masoniteorm.migrations import Migration

class Medication(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("medications") as table:
            table.increments("id")
            table.string("name")
            table.string("dosage")
            table.string("frequency")
            table.string("start_date")
            table.string("end_date")
            table.integer("medicalrecord_id").unsigned()
            table.foreign("medicalrecord_id").references("id").on("medicalrecords")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("medications")
