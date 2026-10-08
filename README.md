## 🚀 Installation

Ce projet utilise [uv](https://docs.astral.sh/uv/) pour la gestion des dépendances.

### 1. Installer uv (si ce n'est pas déjà fait)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Cloner et installer

```bash
git clone https://github.com/TON-USER/wedding-planner-multiagent.git
cd wedding-planner-multiagent
uv sync
```

### 3. Configurer les variables d'environnement

```bash
cp .env.example .env
# Édite .env et remplis tes clés API
```

### 4. Lancer le notebook

```bash
uv run jupyter notebook notebooks/wedding_planner.ipynb
```