document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const name = formData.get('name');
    const email = formData.get('email');

    fetch('http://localhost:5000/store', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
