import Head from 'next/head';

/**
 * Metrics page
 *
 * This page provides a placeholder for displaying high‑level KPIs and
 * metrics about your business. In a real implementation, these values
 * would be pulled from your database or analytics service. Here we
 * simply render static cards styled with your brand palette.
 */
export default function Metrics() {
  return (
    <>
      <Head>
        <title>Metrics · RiskTravel Dashboard</title>
      </Head>
      <main className="container">
        <h1>Key Metrics</h1>
        <p>
          These cards will soon reflect live data from your AI governance
          and retreat business. Use this page to track revenue, leads,
          engagement and other important KPIs.
        </p>
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
            gap: '1rem',
            marginTop: '1rem',
          }}
        >
          {/* Example metric card */}
          <div
            style={{
              background: 'var(--colour-deep-purple)',
              color: 'white',
              padding: '1.5rem',
              borderRadius: '0.5rem',
              boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
            }}
          >
            <h3 style={{ marginTop: 0 }}>Monthly Revenue</h3>
            <p style={{ fontSize: '1.75rem', fontWeight: 600 }}>$0</p>
            <small style={{ opacity: 0.8 }}>Target: $50K</small>
          </div>
          <div
            style={{
              background: 'var(--colour-mid-purple)',
              color: 'white',
              padding: '1.5rem',
              borderRadius: '0.5rem',
              boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
            }}
          >
            <h3 style={{ marginTop: 0 }}>Open Leads</h3>
            <p style={{ fontSize: '1.75rem', fontWeight: 600 }}>0</p>
            <small style={{ opacity: 0.8 }}>Target: 25</small>
          </div>
          <div
            style={{
              background: 'var(--colour-aubergine)',
              color: 'white',
              padding: '1.5rem',
              borderRadius: '0.5rem',
              boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
            }}
          >
            <h3 style={{ marginTop: 0 }}>Retreat Deposits</h3>
            <p style={{ fontSize: '1.75rem', fontWeight: 600 }}>0</p>
            <small style={{ opacity: 0.8 }}>Target: 8 guests</small>
          </div>
          <div
            style={{
              background: 'var(--colour-dark-cyan)',
              color: 'white',
              padding: '1.5rem',
              borderRadius: '0.5rem',
              boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
            }}
          >
            <h3 style={{ marginTop: 0 }}>Video Views</h3>
            <p style={{ fontSize: '1.75rem', fontWeight: 600 }}>0</p>
            <small style={{ opacity: 0.8 }}>Goal: 10K</small>
          </div>
        </div>
      </main>
    </>
  );
}