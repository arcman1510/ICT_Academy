import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Card from './componenti/Card'

function App() {
  const [count, setCount] = useState(0)
  const cities=[
    {id: 0,
      name:"Tokyo",
      desc:"Lorem ipsum dolor sit amet, consectetur adipiscing elit,",
      imgUrl:"https://images.unsplash.com/photo-1732373558548-ccc9f9e83af0?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      isVisit:true,
    },
    {id: 1,
      name:"Tokyo",
      desc:"Lorem ipsum dolor sit amet, consectetur adipiscing elit,",
      imgUrl:"https://images.unsplash.com/photo-1733227085045-0d985de2b9d9?q=80&w=1972&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      isVisit:true,
    },
    {id: 2,
      name:"Tokyo",
      desc:"Lorem ipsum dolor sit amet, consectetur adipiscing elit,",
      imgUrl:"https://images.unsplash.com/photo-1732445027430-fbe0961cb100?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      isVisit:true,
    },
    {id: 3,
      name:"Tokyo",
      desc:"Lorem ipsum dolor sit amet, consectetur adipiscing elit,",
      imgUrl:"https://images.unsplash.com/photo-1733051155541-eaf8979ff01b?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      isVisit:true,
    },



  ]
  return (
    <>
     <Card></Card>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
