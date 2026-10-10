"""03_contact_book.py - Mini project: add, search, and delete contacts."""


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name: str, phone: str, email: str = "") -> None:
        self.contacts[name.lower()] = {"name": name, "phone": phone, "email": email}

    def search(self, text: str) -> list:
        """Find contacts whose name contains the text."""
        text = text.lower()
        return [c for key, c in self.contacts.items() if text in key]

    def delete(self, name: str) -> bool:
        return self.contacts.pop(name.lower(), None) is not None

    def show_all(self) -> None:
        for contact in sorted(self.contacts.values(), key=lambda c: c["name"]):
            print(f"  {contact['name']:<8} {contact['phone']:<14} {contact['email']}")


if __name__ == "__main__":
    book = ContactBook()
    book.add("Ada", "0801-111-2222", "ada@example.com")
    book.add("Adam", "0802-333-4444")
    book.add("Ben", "0803-555-6666", "ben@example.com")

    print("Search 'ad':", [c["name"] for c in book.search("ad")])
    print("Deleted Ben?", book.delete("ben"))
    print("Deleted Zed?", book.delete("zed"))
    print("All contacts:")
    book.show_all()
