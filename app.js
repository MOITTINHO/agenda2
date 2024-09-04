document.getElementById('bookingForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Evita o comportamento padrão de envio do formulário
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;

    console.log('Submitting form with data:', { date, time, name, phone });

    fetch('/book', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            date: date,
            time: time,
            name: name,
            phone: phone
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server response:', data);
        if (data.success) {
            alert(data.success);
            document.getElementById('bookingForm').reset(); // Reseta o formulário
        } else {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
