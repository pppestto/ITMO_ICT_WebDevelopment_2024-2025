# Printing House Frontend (Vue.js 3)

## Описание

Frontend приложение на Vue.js 3 с TypeScript для управления типографией. Взаимодействует с Django REST API.

## Технологии

- Vue.js 3 (Composition API)
- TypeScript
- Vuetify 3 (Material Design)
- Vite (сборщик)
- Pinia (state management)
- axios (HTTP клиент)
- Vue Router (маршрутизация)

## Структура проекта

```
frontend/
├── src/
│   ├── App.vue
│   ├── main.ts
│   ├── components/        # Переиспользуемые компоненты
│   ├── views/            # Страницы приложения
│   ├── services/         # API сервисы
│   ├── stores/           # Pinia хранилища
│   ├── types/            # TypeScript интерфейсы
│   ├── router/           # Vue Router
│   └── plugins/          # Плагины (Vuetify)
│
├── index.html
├── package.json
├── vite.config.ts
└── tsconfig.json
```

## Компоненты

### Основные страницы (views/)
- Даш-борд - главная страница
- Газеты - управление газетами
- Типографии - управление типографиями
- Тиражи - управление тиражами
- Распределение - распределение газет

### Компоненты (components/)
- NewspaperList - таблица газет
- PrintingHouseList - таблица типографий
- PrintingRunForm - форма создания тиража
- DistributionForm - форма распределения

## API Сервисы

### Файл: services/api.ts

```typescript
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8001/api'
});

// Newspapers
export const getNewspapers = (params?: any) => 
  API.get('/newspapers/', { params });

export const createNewspaper = (data: any) => 
  API.post('/newspapers/', data);

export const updateNewspaper = (id: number, data: any) => 
  API.put(`/newspapers/${id}/`, data);

export const deleteNewspaper = (id: number) => 
  API.delete(`/newspapers/${id}/`);

// PrintingHouses
export const getPrintingHouses = () => 
  API.get('/printing-houses/');

export const createPrintingHouse = (data: any) => 
  API.post('/printing-houses/', data);

// PrintingRuns
export const getPrintingRuns = () => 
  API.get('/printing-runs/');

export const createPrintingRun = (data: any) => 
  API.post('/printing-runs/', data);

// Distribution
export const getDistribution = () => 
  API.get('/distribution/');

export const createDistribution = (data: any) => 
  API.post('/distribution/', data);
```

## State Management (Pinia)

### Store структура

```typescript
// stores/printing.ts
import { defineStore } from 'pinia';

export const usePrintingStore = defineStore('printing', () => {
  const newspapers = ref([]);
  const printingHouses = ref([]);
  
  const fetchNewspapers = async () => {
    const res = await getNewspapers();
    newspapers.value = res.data.results;
  };
  
  const addNewspaper = async (data) => {
    await createNewspaper(data);
    await fetchNewspapers();
  };
  
  return {
    newspapers,
    printingHouses,
    fetchNewspapers,
    addNewspaper
  };
});
```

## Использование в компонентах

```vue
<script setup lang="ts">
import { onMounted } from 'vue';
import { usePrintingStore } from '@/stores/printing';

const store = usePrintingStore();

onMounted(() => {
  store.fetchNewspapers();
});
</script>

<template>
  <div>
    <h1>Газеты</h1>
    <div v-for="newspaper in store.newspapers" :key="newspaper.id">
      <p>{{ newspaper.title }}</p>
      <p>{{ newspaper.editor_last_name }} {{ newspaper.editor_first_name }}</p>
    </div>
  </div>
</template>
```

## Маршруты

```typescript
// router/index.ts
const routes = [
  {
    path: '/',
    component: Dashboard
  },
  {
    path: '/newspapers',
    component: NewspapersPage
  },
  {
    path: '/printing-houses',
    component: PrintingHousesPage
  },
  {
    path: '/printing-runs',
    component: PrintingRunsPage
  },
  {
    path: '/distribution',
    component: DistributionPage
  }
];
```

## UI с Vuetify 3

Компоненты используют:
- v-data-table - таблицы
- v-form - формы
- v-dialog - модальные окна
- v-card - карточки
- v-btn - кнопки
- v-text-field - текстовые поля
- v-select - селекты

## Запуск

```bash
cd frontend
npm install
npm run dev
```

Доступно: http://localhost:5173

## Сборка для продакшена

```bash
npm run build
```

Будет создана папка `dist/` с собранным приложением.

## TypeScript типы

```typescript
// types/index.ts
export interface Newspaper {
  id: number;
  title: string;
  publication_index: string;
  editor_first_name: string;
  editor_last_name: string;
  editor_middle_name?: string;
  price_per_copy: string;
}

export interface PrintingHouse {
  id: number;
  name: string;
  address: string;
  is_active: boolean;
}

export interface PrintingRun {
  id: number;
  printing_house: number;
  newspaper: number;
  circulation: number;
}

export interface Distribution {
  id: number;
  post_office: number;
  newspaper: number;
  printing_house: number;
  quantity: number;
}
```

## Обработка ошибок

```typescript
try {
  await store.addNewspaper(formData);
  showSuccess('Газета успешно создана');
} catch (error) {
  showError('Ошибка при создании газеты');
  console.error(error);
}
```

## Адаптивность

Приложение полностью адаптивно с использованием Vuetify grid системы:
- Мобильные устройства
- Планшеты
- Десктопы

Дополнительно: [Вернуться к обзору Lr4](index.md)
