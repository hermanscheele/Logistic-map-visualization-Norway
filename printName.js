





// Create a div element for displaying the municipal ID
const infoBox = document.createElement("div");
infoBox.classList.add("info-box");
infoBox.textContent = "Trykk på kartet!"; // Set the default text here
document.body.appendChild(infoBox);



let previousPath = null; // Variable to store the previously clicked path

// Function to handle the click event on municipal paths
function handleMunicipalClick(event) {
    const clickedPath = event.target;
    const municipalName = clickedPath.getAttribute("inkscape:label");

    clickedPath.style.stroke = 'red';
    clickedPath.style.strokeWidth = '4'; // Set the desired stroke width in pixels

    // Update the info box with the municipal name
    infoBox.textContent = "Kommune navn: " + municipalName;



    if (previousPath && previousPath !== clickedPath) {
        previousPath.style.stroke = ''; // Reset the border color of the previous path
        previousPath.style.strokeWidth = ''; // Reset the stroke width of the previous path
    }

    // Fetch the JSON file
    fetch("data.json")
        .then(response => response.json())
        .then(data => {


            if (municipalName.toUpperCase() in data) {
                const value = data[municipalName.toUpperCase()];
                
                console.log(`${municipalName}: ${value}`);
                infoBox.textContent +=   " Ordre: " + "    " + value 
            }
        
        })
        .catch(error => {
            console.log("Error fetching JSON file:", error);
        });

    previousPath = clickedPath; // Store the current clicked path as the previous path

}

// Fetch the SVG/XML file
fetch("map.svg")
    .then((response) => response.text())
    .then((data) => {
        // Create a new DOM parser
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(data, "image/svg+xml");

        // Retrieve the SVG element and all municipal paths
        const svg = xmlDoc.querySelector("svg");
        const paths = svg.getElementsByTagName("path");

        // Attach click event listener to each municipal path
        for (let i = 0; i < paths.length; i++) {
            const path = paths[i];
            path.addEventListener("click", handleMunicipalClick);
        }

        // Append the SVG to the map-container div
        const mapContainer = document.getElementById("map-container");
        mapContainer.appendChild(svg);
    })
    .catch((error) => {
        console.log("Error loading SVG file:", error);
    });


