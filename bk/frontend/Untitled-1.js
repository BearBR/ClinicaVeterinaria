<script>
document.addEventListener('DOMContentLoaded', () => {
    const API = 'http://127.0.0.1:5000';
    let editandoId = null;

    async function carregarDonos() {
        const r = await fetch(`${API}/api/donos`);
        const dados = await r.json();
        document.getElementById('tbody-donos').innerHTML =
            dados.map(d => `
                <tr data-id="${d.id}">
                    <td>${d.id}</td>
                    <td>
                        <strong>${d.nome}</strong><br />
                        <span class="text-muted">${d.email || ''}</span>
                    </td>
                    <td>${d.telefone || ''}</td>
                    <td>${d.endereco || ''}</td>
                    <td>${d.cep || ''}</td>
                    <td>
                        <button class="btn btn-danger btn-sm me-1" onclick="deletarDono(${d.id})">Excluir</button>
                        <button class="btn btn-warning btn-sm" onclick="editarDono(${d.id})">Editar</button>
                    </td>
                </tr>
            `).join('');
    }

    window.deletarDono = async function(id) {
        if (!confirm('Deseja realmente deletar este dono?')) return;
        const response = await fetch(`${API}/api/donos/${id}`, { method: 'DELETE' });
        if (!response.ok) {
            alert('Erro ao deletar o dono.');
            return;
        }
        alert('Dono deletado com sucesso!');
        carregarDonos();
    };

    window.editarDono = async function(id) {
        const r = await fetch(`${API}/api/donos/${id}`);
        const dono = await r.json();
        document.querySelector('input[name=nome]').value = dono.nome || '';
        document.querySelector('input[name=telefone]').value = dono.telefone || '';
        document.querySelector('input[name=email]').value = dono.email || '';
        document.querySelector('input[name=endereco]').value = dono.endereco || '';
        document.querySelector('input[name=cep]').value = dono.cep || '';
        editandoId = id;
        document.getElementById('submit-btn').textContent = 'Alterar';
    };

    document.getElementById('form-dono').addEventListener('submit', async (e) => {
        e.preventDefault();
        const fd = new FormData(e.target);
        const donoData = Object.fromEntries(fd);

        if (editandoId) {
            await fetch(`${API}/api/donos/${editandoId}`, {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(donoData)
            });
            editandoId = null;
            document.getElementById('submit-btn').textContent = 'Salvar';
        } else {
            await fetch(`${API}/api/donos`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(donoData)
            });
        }

        e.target.reset();
        carregarDonos();
    });

    carregarDonos();
});
</script>
