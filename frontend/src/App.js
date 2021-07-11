
import LeftComponent from './components/leftComponent/LeftComponent'
import Header from './components/header'
import {Container} from 'react-bootstrap'
import App2 from './components/new_calendar'


function App() {
  return (
    <div style={{maxWidth: '1440px', margin: '0 auto'}}>
      <Header/>
      <div style={{display: 'flex', flexDirection: 'row'}}>
        <LeftComponent/>
          <App2/>
      </div>
    </div>
  );
}

export default App;
