
export const NoteReducer = (state = {notes: []}, action) => {
    switch(action.type) {
        case 'success':
            return {...state, notes: action.payload}
        
        case 'error':
            return {error: action.payload}

        default:
            return state
    }
}


export const NoteCalendar = (state = {datas: []}, action) => {
    switch(action.type) {
        case 'success':
            return {...state, datas: action.payload}
        
        case 'error':
            return {error: action.payload}

        default:
            return state
    }
}
