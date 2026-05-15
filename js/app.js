fetch('datos.json')
  .then(response => response.json())
  .then(data => {
      const lista = document.getElementById('lista');
      lista.innerHTML = ''; // limpiar si ya hay contenido
      data.coches.forEach(coche => {
          const li = document.createElement('li');
          li.innerHTML = `
            <h2>${coche.marca} ${coche.modelo}</h2>
            <p><strong>Año:</strong> ${coche.año}</p>
            <p><strong>Motor:</strong> ${coche.motor}</p>
          `;
          lista.appendChild(li);
      });
  })
  .catch(error => console.error('Error cargando JSON:', error));