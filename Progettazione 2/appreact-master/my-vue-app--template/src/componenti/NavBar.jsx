import './NavBar.css'

// creazione constanti
const x = '-----><-----';
const img1 = '/vite.svg'
const img2 = '/src/assets/react.svg'
const imgStyle = {
height: '200px',
borderRadius: '70px'
}

function NavBar(){
    return(
    <>
    <div id = 'box' className='box' ></div>
    <nav> {x}</nav>
    <img src = {img1} height={200}></img>
    <img style={imgStyle} src = {img2}></img>
    <p className='stilemio' > CORSO </p>
    <p color='yellow' >________________</p>

    <ul>
        <li> <a href = "#" > ciao</a></li>
        <li> <a href = "#" > ciao</a></li>
        <li> <a href = "#" > ciao</a></li>
        <li> <a href = "#" > ciao</a></li>       
    </ul>
    </>
    )
}
export default NavBar
