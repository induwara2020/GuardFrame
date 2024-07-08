document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('textForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let inputText = document.getElementById('inputText').value;
    let operation = document.getElementById('operation').value;
    let key = parseInt(document.getElementById('key').value);

    fetch('/caesar_process', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: inputText, operation: operation, key: key })
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('resultText').value = data.result;
    })
    .catch(error => {
      console.error('Error:', error);
      alert('An error occurred. Please try again later.');
    });
  });
});
