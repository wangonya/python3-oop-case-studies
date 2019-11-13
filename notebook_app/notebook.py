import datetime

# store the next available id for all new notes
last_id = 0


class Note:
    """Represent a note in the notebook.
    Match against a string and store tags for each note."""

    def __init__(self, memo, tags=''):
        """initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.today()
        global last_id
        last_id += 1
        self.id = last_id

    def __repr__(self):
        return f"{self.id} - {self.memo}"

    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags."""
        return filter in self.memo or filter in self.tags


class NoteBook:
    """Represent a collection of notes that can be tagged,
    modified and searched"""

    def __init__(self):
        """Initialize notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def update_note(self, note_id, memo='', tags=''):
        """Find memo with the given id and update it"""
        for note in self.notes:
            if note.id == note_id:
                if memo:
                    note.memo = memo
                if tags:
                    note.tags = tags
                break

    def list_all(self):
        """
        List all saved notes
        :return: all notes in self.notes[]
        :rtype: list
        """
        return self.notes

    def search(self, filter):
        """Find all notes that match the given filter string"""
        return [note for note in self.notes if note.match(filter)]
