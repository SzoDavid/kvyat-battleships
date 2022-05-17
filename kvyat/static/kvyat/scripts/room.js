let model = {
    boardSize: 7,
    numShips: 3,
    shipLength: 3,
    shipsSunk: 0,

    ships:[
        { locations: [0, 0, 0], hits: ["", "", ""] },
        { locations: [0, 0, 0], hits: ["", "", ""] },
        { locations: [0, 0, 0], hits: ["", "", ""] }
    ],

    fire: function(guess) {
        for (let i = 0; i < this.numShips; i++) {
            let ship = this.ships[i];
            let index = ship.locations.indexOf(guess);
            if (ship.hits[index] === "hit") {
                view.displayMessage("You hit this ship before.");
                return true;
            } else if (index >= 0) {
                ship.hits[index] = "hit";
                view.displayHit(guess);
                view.displayMessage("It's a hit!");
                if (this.isSunk(ship)) {
                    view.displayMessage("You sank my battleship!");
                    this.shipsSunk++;
                }
                return true;
            }
        }
        view.displayMiss(guess);
        view.displayMessage("It's a miss!");
        return false;
    },

    isSunk: function(ship) {
        for (let i = 0; i < this.shipLength; i++) {
            if (ship.hits[i] !== "hit") {
                return false;
            }
        }
        return true;
    },

    generateShipLocations: function() {
        let locations;
        let direction;
        for (let i = 0; i < this.numShips; i++) {
            do {
                let result = this.generateShip();
                locations = result[0];
                direction = result[1];
            } while (this.collision(locations, direction));
            this.ships[i].locations = locations;
        }
        console.log("Ship table: ");
        console.log(this.ships);
    },

    generateShip: function() {
        let direction = Math.floor(Math.random() * 2);
        let row, col;

        if (direction === 1) {  // horizontal
            row = Math.floor(Math.random() * this.boardSize);
            col = Math.floor(Math.random() * (this.boardSize - this.shipLength));
        } else { // vertical
            row = Math.floor(Math.random() * (this.boardSize - this.shipLength));
            col = Math.floor(Math.random() * this.boardSize);
        }

        let newShipLocations = [];
        for (let i = 0; i < this.shipLength; i++) {
            if (direction === 1) {
                newShipLocations.push(row + "" + (col + i));
            } else {
                newShipLocations.push((row + i) + "" + col);
            }
        }
        return [newShipLocations, direction];
    },

    collision: function(locations, direction) {
        for (let i = 0; i < this.numShips; i++) {
            let ship = this.ships[i];
            for (let j = 0; j < locations.length; j++) {
                for (let k = 0; k < this.shipLength; k++) {
                    let index
                    if (direction === 1) index = j + k;
                    else index = j + 10 * k;
                    if (ship.locations.indexOf(locations[index]) >= 0) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

};

let view = {
    displayMessage: function(msg) {
        let messageArea = document.getElementById("messageArea");
        messageArea.innerHTML = msg;
    },

    displayHit: function(location) {
        let cell = document.getElementById(location);
        cell.setAttribute("class","hit");

    },

    displayMiss: function(location) {
        let cell = document.getElementById(location);
        cell.setAttribute("class","miss");
    }
};

let controller = {
    guesses: 0,
    processGuess: function(location) {
        if (location) {
            this.guesses++;
            let hit = model.fire(location);
            if (hit && model.shipsSunk === model.numShips) {
                view.displayMessage("You sank all of my battleships in " + this.guesses + " tries.");
                document.getElementById("guessInput").style.visibility = "collapse";
                document.getElementById("returnButton").style.visibility = "visible";
            }
        }
    }
}

window.onload = init;

function init() {

    let guessClick = document.getElementsByTagName("td");
    for (let i = 0; i < guessClick.length; i++) {
        guessClick[i].onclick = answer;
    }

    model.generateShipLocations();
    view.displayMessage("Hello, let's play! There are 3 ships, each 3 cells long!");
}

function answer(eventObj) {
    let shot = eventObj.target;
    let location = shot.id;
    controller.processGuess(location);
}

function returnAction(base_url) {
    document.location.href = base_url.replace('123', controller.guesses);
}

