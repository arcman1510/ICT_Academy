import { useState, useEffect } from 'react';
import axios from 'axios';

const Axios = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/1')
      .then((response) => {
        setUsers(response.data);  
        setLoading(false);         
      })
      .catch((error) => {
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Caricamento...</p>;
  if (error) return <p>Errore: {error}</p>;

  return (
    <div>
      <h1 className='font'>ELENCO PROGETTI:</h1>
      <ul>
      <table>
      <thead>
        <tr>
            <th>ID</th>
            <th>ID Progetto</th>
            <th>Nome WP</th>
            <th>Inizio Progetto</th>
            <th>Fine Progetto</th>
        </tr>
        </thead>
        {users.map((user) => (
          //<li key={user.id}>{user.progetto} - {user.nome} - {user.inizio} - {user.fine}</li>
          <tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.progetto}</td>
            <td>{user.nome}</td>
            <td>{user.inizio}</td>
            <td>{user.fine}</td>
          </tr>
        ))}
      </table>
      </ul>
    </div>
  );
};

export default Axios;