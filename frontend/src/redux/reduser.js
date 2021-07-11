
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
