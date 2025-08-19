import Head from 'next/head';

/**
 * Home page for the RiskTravel dashboard.
 *
 * This simple landing page serves as the entry point for your future admin
 * dashboard. As the project evolves, you'll replace this content with
 * authentication, navigation, and dynamic data sourced from your CRM and
 * automation agents.
 */
export default function Home() {
  return (
    <>
      <Head>
        <title>RiskTravel Dashboard</title>
        <meta name="description" content="Admin dashboard for the RiskTravel empire" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <main className="container" style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
        <h1 style={{ fontSize: '2rem', marginBottom: '1rem' }}>RiskTravel Dashboard</h1>
        <p>
          Welcome! This project provides the foundation for the admin dashboard
          powering your AI governance and retreat business. Over time this page
          will evolve into a fully featured dashboard with real‑time metrics,
          agent controls, and workflows tailored to your specific needs.
        </p>
        <p>
          To get started, run <code>npm install</code> followed by
          <code> npm run dev</code> to launch a local development server. Then
          point your browser to <code>http://localhost:3000</code>.
        </p>
      </main>
    </>
  );
}