import axios from 'axios'


export const NoteActions = (date) => async (dispatch) => {
    try {
        const {month, day} = date
        const url = 'http://localhost:3000/notes'

        if (day==6) {
        const {data} = await axios({
            headers: {
                "Content-Type": "application/json",
             },
             
            url: url
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