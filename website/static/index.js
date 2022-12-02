function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }), //This is the note Id attribute accessed in views.py
    }).then((_res) => {
      window.location.href = "/";
    });
  }

