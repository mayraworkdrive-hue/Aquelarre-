# Aquelarre ✨  
**Lecturas místicas con IA · Entretenimiento puro · 2 consultas gratis, luego 0.01 USD por lectura**

https://aquelarre.app (próximamente)

Una experiencia de tarot, oráculos y magia generada 100 % con inteligencia artificial.  
Esto NO es videncia real: es puro entretenimiento, humor negro y estética bruja muy cuidada.

## Demo en vivo (ya funciona)
https://aquelarre-mistica.vercel.app

## Stack completo
- Frontend → React 19 + Vite + Tailwind CSS + shadcn/ui  
- Backend → FastAPI (Python 3.11)  
- Base de datos → SQLite (dev) / PostgreSQL (producción)  
- IA texto → Groq + Llama-3.1-70B-Instant (gratis y ultra-rápido)  
- IA imágenes → Flux.1-dev vía Groq o Black-Forest-Labs  
- Pagos → Stripe Checkout (soporta 0.01 USD y modo test activado)  
- Deploy → Vercel (frontend) + Render / Railway (backend)

## Cómo correrlo en tu máquina (2 minutos)

### 1. Clona y entra
```bash
git clone https://github.com/tarot-luna/aquelarre.git
cd aquelarre
