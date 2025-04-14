document.getElementById('dietForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  // Show loading, hide results and error
  document.querySelector('.loading').style.display = 'block';
  document.getElementById('results').style.display = 'none';
  document.getElementById('errorMessage').style.display = 'none';
  
  const formData = {
      weight: parseFloat(document.getElementById('weight').value),
      height: parseFloat(document.getElementById('height').value),
      age: parseInt(document.getElementById('age').value),
      gender: document.getElementById('gender').value,
      activity: document.getElementById('activity').value,
      is_vegetarian: document.getElementById('is_vegetarian').value,
      diet_type: document.getElementById('diet_type').value
  };

  try {
      const response = await fetch('/calculate', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
      });

      const data = await response.json();

      if (response.ok) {
          // Update calories
          document.getElementById('baseCalories').textContent = data.calories.base;
          document.getElementById('bulkCalories').textContent = data.calories.bulk;
          document.getElementById('cutCalories').textContent = data.calories.cut;

          // Update meal tables
          updateMealTable('breakfastTable', data.meal_plan.breakfast);
          updateMealTable('lunchTable', data.meal_plan.lunch);
          updateMealTable('dinnerTable', data.meal_plan.dinner);

          // Hide loading, show results
          document.querySelector('.loading').style.display = 'none';
          document.getElementById('results').style.display = 'block';
      } else {
          throw new Error(data.error || 'An error occurred');
      }
  } catch (error) {
      // Hide loading, show error
      document.querySelector('.loading').style.display = 'none';
      const errorMessage = document.getElementById('errorMessage');
      errorMessage.textContent = error.message;
      errorMessage.style.display = 'block';
  }
});

function updateMealTable(tableId, meals) {
  const table = document.getElementById(tableId);
  table.innerHTML = '';

  meals.forEach(meal => {
      const row = document.createElement('tr');
      row.innerHTML = `
          <td class="food-item">${meal['Food_Item']}</td>
          <td><span class="nutrition-badge">${Math.round(meal['Calories (kcal)'])} kcal</span></td>
          <td><span class="nutrition-badge">${Math.round(meal['Protein (g)'])}g</span></td>
          <td><span class="nutrition-badge">${Math.round(meal['Fiber (g)'])}g</span></td>
      `;
      table.appendChild(row);
  });
}