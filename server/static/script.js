document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    fetch('/predict', {
        method: 'POST',
        body: new FormData(document.getElementById('predictionForm'))
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerHTML = '<h2>Price: €' + data.predicted_price + '</h2>';
    })
    .catch(error => console.error('Error:', error));
});
