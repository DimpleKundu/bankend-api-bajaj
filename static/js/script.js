document.getElementById('api-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form from submitting the usual way
    
    // Get form data
    const dataInput = document.getElementById('data').value.split(',');
    const fileInput = document.getElementById('file').files[0];
    
    // Prepare the form data
    let formData = {
        data: dataInput
    };

    if (fileInput) {
        // Convert the file to base64 if it's present
        const reader = new FileReader();
        
        reader.onloadend = function () {
            formData.file_b64 = reader.result.split(',')[1]; // Extract base64 data

            // Send the POST request with file data
            sendPostRequest(formData);
        };
        
        reader.readAsDataURL(fileInput);
    } else {
        // Send the POST request without file
        sendPostRequest(formData);
    }
});

function sendPostRequest(formData) {
    fetch('https://bjaj-finserv-fsd-rest-api.vercel.app/bfhl', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        // Display the response in the result div
        document.getElementById('response-output').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('response-output').textContent = 'An error occurred while processing your request.';
    });
}
