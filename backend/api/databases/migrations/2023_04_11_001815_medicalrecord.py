"""Medicalrecord Migration."""

from masoniteorm.migrations import Migration

class Medicalrecord(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("medical_records") as table:
            table.increments("id")
            table.string("date")
            table.string("diagnosis")
            table.integer("patient_id").unsigned()
            table.foreign("patient_id").references("id").on("patients")
            table.timestamps()
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("medical_records")
