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
      <main className="container">
        <h1>Welcome to RiskTravel</h1>
        <p>
          This scaffold provides the foundation for your admin dashboard,
          which will eventually display real‑time metrics, agent statuses and
          workflows tailored to your AI governance and retreat business.
        </p>
        <p>
          Next steps include connecting your data sources (Airtable, Postgres
          or similar), building pages for agents, metrics and CRM, and
          integrating automation workflows. Use the navigation links above to
          explore new pages as you add them.
        </p>
      </main>
    </>
  );
}