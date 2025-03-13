<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" indent="yes"/>

<xsl:template match="/">
  <html>
    <head>
      <title>Evidenta Pacienti - Toate Tabelele</title>
    </head>
    <body>
      <h1>Evidenta Pacienti - Toate Tabelele</h1>

      <!-- Tabelul pentru pacienti -->
      <h2>Lista Pacientilor</h2>
      <table border="1">
        <tr>
          <th>ID Pacient</th>
          <th>Nume Pacient</th>
          <th>Varsta Pacient</th>
        </tr>
        <xsl:for-each select="evidenta_pacienti/pacient">
          <tr>
            <td><xsl:value-of select="@id"/></td>
            <td><xsl:value-of select="nume"/></td>
            <td><xsl:value-of select="varsta"/></td>
          </tr>
        </xsl:for-each>
      </table>

      <!-- Tabelul pentru fiecare pacient cu tratamentele sale -->
      <xsl:for-each select="evidenta_pacienti/pacient">
        <h2>Pacient: <xsl:value-of select="nume"/></h2>
        <table border="1">
          <tr>
            <th>Nume Tratament</th>
            <th>Dozaj</th>
            <th>Frecventa</th>
          </tr>
          <xsl:for-each select="tratament">
            <tr>
              <td><xsl:value-of select="denumire"/></td>
              <td><xsl:value-of select="doza"/></td>
              <td><xsl:value-of select="frecventa"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </xsl:for-each>

      <!-- Tabelul pentru toate tratamentele -->
      <h2>Lista Tuturor Tratamentelelor</h2>
      <table border="1">
        <tr>
          <th>Nume Tratament</th>
          <th>ID Pacient</th>
          <th>Nume Pacient</th>
          <th>Dozaj</th>
          <th>Frecventa</th>
        </tr>
        <xsl:for-each select="evidenta_pacienti/pacient/tratament">
          <tr>
            <td><xsl:value-of select="denumire"/></td>
            <td><xsl:value-of select="../@id"/></td>
            <td><xsl:value-of select="../nume"/></td>
            <td><xsl:value-of select="doza"/></td>
            <td><xsl:value-of select="frecventa"/></td>
          </tr>
        </xsl:for-each>
      </table>

    </body>
  </html>
</xsl:template>

</xsl:stylesheet>