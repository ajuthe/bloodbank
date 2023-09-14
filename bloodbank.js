document.addEventListener("DOMContentLoaded", function () {
    const contentDiv = document.getElementById("content");

    // Function to display content in the "content" div
    function displayContent(content) {
        contentDiv.innerHTML = content;
    }

    // Function to send AJAX requests and handle responses
    function sendAjaxRequest(url, method, data, successCallback, errorCallback) {
        fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.json();
            })
            .then(successCallback)
            .catch(errorCallback);
    }

    // Event listener for "Check Blood Availability" button
    document.getElementById("checkBtn").addEventListener("click", () => {
        const content = `
            <h2>Check Blood Availability</h2>
            <label for="bloodType">Enter blood type:</label>
            <input type="text" id="bloodType">
            <button id="checkAvailabilityBtn">Check Availability</button>
            <div id="availabilityResult"></div>
        `;

        displayContent(content);

        // Event listener for "Check Availability" button
        document.getElementById("checkAvailabilityBtn").addEventListener("click", () => {
            const bloodType = document.getElementById("bloodType").value;
            sendAjaxRequest(
                "/check_availability",
                "POST",
                { "blood_type": bloodType },
                (data) => {
                    const availabilityResult = document.getElementById("availabilityResult");
                    availabilityResult.textContent = `Available units of ${bloodType}: ${data.availability}`;
                },
                (error) => {
                    console.error("Error:", error);
                }
            );
        });
    });

    // Add similar event listeners for "Donate Blood" and "Distribute Blood" buttons
});
