import Head from 'next/head';

/**
 * Agents page
 *
 * This page provides a placeholder for monitoring the status of your
 * automation agents. In a full implementation this would fetch live
 * agent data from your database or API and display it in a table or
 * dashboard. For now, we include static content to illustrate the
 * structure and styling.
 */
export default function Agents() {
  return (
    <>
      <Head>
        <title>Agents · RiskTravel Dashboard</title>
      </Head>
      <main className="container">
        <h1>Automation Agents</h1>
        <p>
          Monitor the status, last run time and success rate of your
          automation agents here. As you build out your agent fleet,
          populate this table with data from your Airtable base or
          database.
        </p>
        <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '1rem' }}>
          <thead>
            <tr style={{ backgroundColor: 'var(--colour-mid-purple)', color: 'white' }}>
              <th style={{ padding: '0.5rem', textAlign: 'left' }}>Agent Name</th>
              <th style={{ padding: '0.5rem', textAlign: 'left' }}>Description</th>
              <th style={{ padding: '0.5rem', textAlign: 'left' }}>Status</th>
              <th style={{ padding: '0.5rem', textAlign: 'left' }}>Last Run</th>
            </tr>
          </thead>
          <tbody>
            {/* Static example rows; replace with dynamic content later */}
            <tr style={{ backgroundColor: '#f5f5fa' }}>
              <td style={{ padding: '0.5rem' }}>Outreach Agent</td>
              <td style={{ padding: '0.5rem' }}>Generates and sends tailored outreach messages</td>
              <td style={{ padding: '0.5rem' }}>Idle</td>
              <td style={{ padding: '0.5rem' }}>–</td>
            </tr>
            <tr>
              <td style={{ padding: '0.5rem' }}>Content Repurposer</td>
              <td style={{ padding: '0.5rem' }}>Creates social media posts and blog drafts</td>
              <td style={{ padding: '0.5rem' }}>Running</td>
              <td style={{ padding: '0.5rem' }}>Aug 19, 2025 10:15am</td>
            </tr>
            <tr style={{ backgroundColor: '#f5f5fa' }}>
              <td style={{ padding: '0.5rem' }}>Booking/CRM</td>
              <td style={{ padding: '0.5rem' }}>Synchronises Calendly bookings to your CRM</td>
              <td style={{ padding: '0.5rem' }}>Idle</td>
              <td style={{ padding: '0.5rem' }}>–</td>
            </tr>
            <tr>
              <td style={{ padding: '0.5rem' }}>Analytics</td>
              <td style={{ padding: '0.5rem' }}>Tracks metrics and generates weekly reports</td>
              <td style={{ padding: '0.5rem' }}>Paused</td>
              <td style={{ padding: '0.5rem' }}>Aug 18, 2025 9:00am</td>
            </tr>
          </tbody>
        </table>
      </main>
    </>
  );
}