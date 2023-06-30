/* If I want to add my own Javascript */
function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/blog";
  });
}
/* Delete plant */

function deletePlant(plantId) {
  fetch("/delete-plant", {
    method: "POST",
    body: JSON.stringify({ plantId: plantId }),
  }).then((_res) => {
    window.location.href = "/market";
  });
}