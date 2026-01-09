# NextJS

NextJS is a popular React-based framework for building production-ready web applications. It provides features like server-side rendering (SSR), static site generation (SSG), API routes, and file-based routing.

## Key Features

- **File-based Routing**: Pages in the `pages/` directory automatically become routes
- **API Routes**: Create API endpoints in the `pages/api/` directory
- **Server-Side Rendering (SSR)**: Render pages on the server for better SEO and performance
- **Static Site Generation (SSG)**: Pre-build pages at build time for optimal performance
- **Incremental Static Regeneration (ISR)**: Update static pages after build time
- **Built-in CSS and Sass Support**: Style components with CSS Modules, styled-jsx, or Tailwind CSS
- **Automatic Code Splitting**: Optimize bundle size automatically
- **Fast Refresh**: Improved development experience with instant feedback

## Common Commands

- `npm run dev` - Start development server
- `npm run build` - Build the application for production
- `npm start` - Start production server

## Project Structure

```
my-nextjs-app/
├── pages/
│   ├── index.js
│   └── api/
│       └── hello.js
├── public/
├── styles/
└── package.json
```

## File-based Routing

- `pages/index.js` → `/`
- `pages/about.js` → `/about`
- `pages/posts/[id].js` → `/posts/:id`

## API Routes

```javascript
// pages/api/hello.js
export default function handler(req, res) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

## Data Fetching Methods

1. **getStaticProps** - For SSG, runs at build time
2. **getStaticPaths** - For dynamic SSG, defines paths to pre-render
3. **getServerSideProps** - For SSR, runs on each request
4. **SWR** - Client-side data fetching with caching and revalidation

## Environment Variables

```javascript
// .env.local
NEXT_PUBLIC_BASE_URL=https://example.com
DB_HOST=localhost
```

Access with `process.env.NEXT_PUBLIC_*` for client-side or any variable for server-side.

## Image Optimization

NextJS provides an `Image` component with automatic optimization:

```jsx
import Image from 'next/image'

function MyComponent() {
  return (
    <Image
      src="/path/to/image.jpg"
      alt="Description"
      width={500}
      height={500}
    />
  )
}
```

## Link Component

Use the `Link` component for client-side navigation:

```jsx
import Link from 'next/link'

function MyComponent() {
  return (
    <Link href="/about">
      <a>About Page</a>
    </Link>
  )
}
```