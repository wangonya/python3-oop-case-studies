# notebook_app.notebook

## Note
```python
Note(self, memo, tags='')
```
Represent a note in the notebook.
Match against a string and store tags for each note.
### match
```python
Note.match(self, filter)
```
Determine if this note matches the filter
text. Return True if it matches, False otherwise.
Search is case sensitive and matches both text and
tags.
## NoteBook
```python
NoteBook(self)
```
Represent a collection of notes that can be tagged,
modified and searched
### new_note
```python
NoteBook.new_note(self, memo, tags='')
```
Create a new note and add it to the list
### update_note
```python
NoteBook.update_note(self, note_id, memo='', tags='')
```
Find memo with the given id and update it
### list_all
```python
NoteBook.list_all(self)
```

List all saved notes

:return: all notes in self.notes[]
:rtype: list

### search
```python
NoteBook.search(self, filter)
```
Find all notes that match the given filter string
