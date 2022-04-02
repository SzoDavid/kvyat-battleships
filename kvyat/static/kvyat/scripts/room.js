let data = {
    num_ships: 0,
    player: [],
    enemy: [],
    ships_left: {
        four: 1,
        three: 2,
        two: 3,
        one: 4,
    },
}

class ValidationData {
    constructor(value, type) {
        this.value = value
        this.type = type
    }
}

function generateArray(array) {
    for (let i = 0; i < 10; i++) {
        array[i] = new Array(10);
        for (let j = 0; j < 10; j++){
            array[i][j] = null;
        }

    }
    console.log(array)
}

function validate(e) {
    let x = parseInt(e.id[1])
    let y = parseInt(e.id[2])
    // TODO: validate ship placement
    if (data.num_ships === 0) {
        data.ships_left.one--
        return new ValidationData(true, 1)
    }
    else {
        let top_left = null;
        let top = null;
        let top_right = null;
        let left = null;
        let right = null;
        let bottom_left = null;
        let bottom = null;
        let bottom_right = null;

        try {
            top_left = data.player[x - 1][y + 1]
        } catch (e) {}

        try {
            top = data.player[x][y + 1]
        } catch (e) {}

        try {
            top_right = data.player[x + 1][y + 1]
        } catch (e) {}

        try {
            left = data.player[x - 1][y]
        } catch (e) {}

        try {
            right = data.player[x + 1][y]
        } catch (e) {}

        try {
            bottom_left = data.player[x - 1][y - 1]
        } catch (e) {}

        try {
            bottom = data.player[x][y - 1]
        } catch (e) {}

        try {
            bottom_right = data.player[x + 1][y - 1]
        } catch (e) {}

        if ((top_left !== null || top_right !== null || bottom_left !== null || bottom_right !== null) ||
            ((top !== null || bottom !== null) && (left !== null || right !== null))) {
            return new ValidationData(false, null)
        }

        if (top === null && bottom === null && left === null && right === null && data.ships_left.one > 0) {
            data.ships_left.one--
            return new ValidationData(true, 1)
        }
    }

    return new ValidationData(false, null)
}

function onClick(e) {
    console.log(e.id)

    const type = e.id[0]
    const x = parseInt(e.id[1])
    const y = parseInt(e.id[2])

    let validation = validate(e)

    if (type === 'p' && validation.value && data.num_ships < 20 && data.player[x][y] === null) {
        e.style.backgroundColor = '#a9d5fe'
        if (validation.type === 1)
            data.player[x][y] = validation.type
        data.num_ships++

    } else if (type === 'e' && data.enemy[x][y] !== "bombed") {
        e.style.backgroundColor = '#82a1b399'
        data.enemy[x][y] = "bombed"
    }

    console.log(data)
}

function init() {
    generateArray(data.player)
    generateArray(data.enemy)
}

init()
