import unittest
from resume_analyzer.contact_redaction import redact_contacts


class ContactRedactionTests(unittest.TestCase):
    def test_redacts_email(self):
        self.assertNotIn("alex@example.com", redact_contacts("alex@example.com"))

    def test_redacts_phone(self):
        self.assertNotIn("98765-43210", redact_contacts("Call 98765-43210"))


if __name__ == "__main__":
    unittest.main()
