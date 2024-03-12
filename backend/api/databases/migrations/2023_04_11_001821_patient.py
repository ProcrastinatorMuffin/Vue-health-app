"""Patient Migration."""

from masoniteorm.migrations import Migration

class Patient(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("patients") as table:
            table.increments("id")
            table.string("name")
            table.string("email")
            table.string("dob")
            table.string("phone_number", 11).nullable()
            table.enum("gender", ["male", "female"]).nullable()
            table.text("address")
            table.string("status")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("patients")
