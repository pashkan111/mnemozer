import axios from 'axios'


export const NoteActions = (date) => async (dispatch) => {
    try {
        const {month, day, year} = date
        const url = 'http://127.0.0.1:5000/notes'
        if (day && month && year) {
            const dateToDispatch = `${year}.${month}.${day}`
            console.log(dateToDispatch)

        const {data} = await axios({
            headers: {
                "Content-Type": "application/json",
             },
            url: 'http://127.0.0.1:5000/notes',
            data: {"date": dateToDispatch},
            method: "POST"
        })

        dispatch({
            type: 'success',
            payload: data
        })
    }
    } catch (error) {
        dispatch({
            type: 'error',
            payload: error
        })
    }
}

export const NoteCalendar = (data) => async (dispatch) => {
    try {
        const {month} = data
        const {data} = await axios({
            headers: {
                "Content-Type": "application/json",
             },
            url: 'http://127.0.0.1:5000/notes-month',
            data: {"month": month},
            method: "POST"
        })
        dispatch({
            type: 'success',
            payload: data
        })
    } catch (error) {
        dispatch({
            type: 'error',
            payload: error
        })
    }
}